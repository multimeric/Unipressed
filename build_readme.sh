poetry run jupyter nbconvert README.ipynb \
    --to markdown \
    --TemplateExporter.exclude_input_prompt True \
    --TagRemovePreprocessor.remove_cell_tags hide-cell