# import the module

from adm.modules.stage2_decode.decode_wrapper import Decoder_Wrapper
from open_clip.factory import get_model_config, list_models

from adm.modules.stage2_decode.clip_video_spec import CLIP_Video_Spec_v2

import json

def main():
    
    # Assert that the function is callable
    assert callable(get_model_config), "get_model_config is not callable"
    print("Import sucessful: get_model_config is callable.")

    # List available model
    models_avail = list_models()
    for model in models_avail:
        print(model)

    first_stage_config = get_model_config("audio_contrastive_pretrained")
    first_stage_config['target'] = 'modules.stage2_decode.clip_video_spec.CLIP_Video_Spec_v2'

    # Debug
    
    print("PANYA:", CLIP_Video_Spec_v2)

    # Pretty-printing the JSON
    pretty_json = json.dumps(first_stage_config, indent=4, sort_keys=True)
    print(pretty_json)

    # Create an instance of Decoder_Wrapper
    decoder_wrapper = Decoder_Wrapper(
        first_stage_config = first_stage_config,
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