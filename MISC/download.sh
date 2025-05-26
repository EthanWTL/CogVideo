export HF_HOME=/project/sds-rise/ethan/CogVideo/huggingface

python inference/cli_demo.py --prompt "a running car" --model_path THUDM/CogVideoX1.5-5B-I2V --generate_type i2v --image_or_video_path "brz_cropped.png"