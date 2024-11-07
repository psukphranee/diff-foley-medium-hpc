# test_decoder_wrapper.py
import torch
import importlib.util
import os

# Path to decode_wrapper.py file
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules', 'stage2_decode', 'decode_wrapper.py'))

# Load the module
spec = importlib.util.spec_from_file_location("decode_wrapper", module_path)
decode_wrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(decode_wrapper)

# Access the Decoder_Wrapper class
Decoder_Wrapper = decode_wrapper.Decoder_Wrapper


# Define a test function to check basic functionality of Decoder_Wrapper
def test_decoder_wrapper():
    # Define dummy parameters (update with actual parameters if known)
    first_stage_model = None  # Replace with an actual model if required by the constructor
    some_param = 512  # Hypothetical parameter
    
    # Instantiate the Decoder_Wrapper class
    model = Decoder_Wrapper(first_stage_model=first_stage_model, param=some_param)

    # Generate dummy input data for testing
    input_data = torch.randn(1, 3, 256, 256)  # Modify dimensions as required by the model
    
    # Test the forward pass (assuming Decoder_Wrapper has a `forward` method)
    try:
        output = model(input_data)
        print("Output shape:", output.shape)
        
        # Example assertion (update based on the expected output)
        assert output.shape == (1, 3, 256, 256), "Output shape mismatch"
        
        print("Decoder_Wrapper functionality test passed.")
    except Exception as e:
        print("Decoder_Wrapper functionality test failed:", e)

if __name__ == "__main__":
    test_decoder_wrapper()
