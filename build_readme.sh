poetry run jupyter nbconvert README.ipynb \
    --to markdown \
    --TemplateExporter.exclude_input_prompt True \
    --TagRemovePreprocessor.remove_cell_tags hide-cell \
    --TagRemovePreprocessor.remove_all_outputs_tags hide-output #\
    # --execute