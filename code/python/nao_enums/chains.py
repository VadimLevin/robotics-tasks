class Chains:
    Head = "Head"
    LArm = "LArm"
    RArm = "RArm"
    LLeg = "LLeg"
    RLeg = "RLeg"

    def __init__(self):
        pass

    @staticmethod
    def list():
        return [chain_name for chain_name in dir(Chains)
                if not (chain_name.startswith("__") or chain_name is 'list')]
