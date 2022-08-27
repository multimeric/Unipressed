# Note: rerun the notebook manually before doing this.
# Using --execute in this command doesn't execute the hidden
# cells which breaks the build
poetry run jupyter nbconvert README.ipynb \
    --to markdown \
    --TemplateExporter.exclude_input_prompt True \
    --TagRemovePreprocessor.remove_cell_tags hide-cell \
    --TagRemovePreprocessor.remove_all_outputs_tags hide-output