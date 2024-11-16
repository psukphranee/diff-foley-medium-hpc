# import the module

from adm.modules.stage2_decode.decode_wrapper import Decoder_Wrapper

def main():
    # Define a mock configuration for the instance
    config = {
        "first_stage_key": "first_stage",
        "cond_stage_key": "condition_stage",
        "num_training_steps": 100,
    }

    # Create an instance of Decoder_Wrapper
    decoder_wrapper = Decoder_Wrapper(
        first_stage_key=config["first_stage_key"],
        cond_stage_key=config["cond_stage_key"],
        num_training_steps=config["num_training_steps"],
    )

    # Create mock input data
    batch_size = 4
    channels = 3
    height = 64
    width = 64
    input_data = torch.randn(batch_size, channels, height, width)

    # Example usage: Call forward or similar method (if implemented)
    try:
        output = decoder_wrapper.forward(input_data)
        print("Output from Decoder_Wrapper instance:", output)
    except AttributeError as e:
        print("The forward method is not implemented or cannot be used:", e)

if __name__ == "__main__":
    main()