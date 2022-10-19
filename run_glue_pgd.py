python3 Model/run_glue_pgd.py --data_dir Data --model_type bert --model_name_or_path BertConfig --task_name classification_text --output_dir Output
"--model_type", default=None, type=str, required=True,
                        help="Model type selected in the list: " + ", ".join(MODEL_CLASSES.keys()))
    parser.add_argument("--model_name_or_path", default=None, type=str, required=True,
                        help="Path to pre-trained model or shortcut name selected in the list: " + ", ".join(ALL_MODELS))
    parser.add_argument("--task_name", default=None, type=str, required=True,
                        help="The name of the task to train selected in the list: " + ", ".join(processors.keys()))
    parser.add_argument("--output_dir",


     --data_dir, --model_type, --model_name_or_path, --task_name, --output_dir