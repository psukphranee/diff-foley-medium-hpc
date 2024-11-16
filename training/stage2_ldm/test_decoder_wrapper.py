# import the module

from adm.modules.stage2_decode.decode_wrapper import Decoder_Wrapper
from open_clip.factory import get_model_config

def main():
    
    # Assert that the function is callable
    assert callable(get_model_config), "get_model_config is not callable"
    print("get_model_config is callable.")


    # Create an instance of Decoder_Wrapper
    decoder_wrapper = Decoder_Wrapper(
        first_stage_config = config,
        decoder_config=None,
        scheduler_config=None,
        monitor=None
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