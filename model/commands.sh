onmt-build-vocab --size 10000 --save_vocab src-cd-vocab.txt src-cd-train.txt
onmt-build-vocab --size 10000 --save_vocab tgt-cd-vocab.txt tgt-cd-train.txt

onmt-main --model_type Transformer --config data.yml --auto_config train --with_eval