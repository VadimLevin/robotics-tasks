class Postures:
    StandInit = u"StandInit"
    Stand = u"Stand"
    StandZero = u"StandZero"
    Sit = u"Sit"
    SitRelax = u"SitRelax"
    Crouch = u"Crouch"
    LyingBack = u"LyingBack"
    LyingBelly = u"LyingBelly"

    def __init__(self):
        pass

    @staticmethod
    def list():
        return [posture_name for posture_name in dir(Postures)
                if not posture_name.startswith("__") and posture_name is not 'list']
