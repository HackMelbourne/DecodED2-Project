from pygame import mixer

mixer.init()

player_shoot = mixer.Sound("sounds/voice_shoot.wav")
player_shoot.set_volume(0)

player_hit = mixer.Sound("sounds/voice_player_hit.wav")
player_hit.set_volume(0)

player_death = mixer.Sound("sounds/voice_player_death.wav")
player_death.set_volume(0)

enemy_death = mixer.Sound("sounds/voice_enemy_death.wav")
enemy_death.set_volume(0)