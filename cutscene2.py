import pygame
from moviepy.editor import VideoFileClip, AudioFileClip

class Cutscene2:
    def __init__(self, screen):
        self.screen = screen
        self.video = VideoFileClip("cutscenes/airpod-unlock.mp4")
        self.audio = self.video.audio  # Extract the audio track
        self.playing = False
        self.current_frame = 0
        self.audio_channel = None  # For handling audio in Pygame

    def start(self):
        self.playing = True
        self.current_frame = 0
        # Convert audio to a playable file for Pygame
        self.audio.write_audiofile("cutscenes/temp_audio.wav", fps=44100, logger=None)
        self.audio_channel = pygame.mixer.Sound("cutscenes/temp_audio.wav")
        self.audio_channel.play()

    def run(self, events, elapsed_time):
        if self.playing:
            # Get the current video frame
            frame = self.video.get_frame(self.current_frame / 80)
            frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

            # Scale and blit the frame
            frame_surface = pygame.transform.scale(frame_surface, self.screen.get_size())
            self.screen.blit(frame_surface, (0, 0))

            self.current_frame += 1

            # Stop when the video is over
            if self.current_frame >= 100 * self.video.duration:
                self.playing = False
                if self.audio_channel:
                    self.audio_channel.fadeout(500)  # Stop the audio
