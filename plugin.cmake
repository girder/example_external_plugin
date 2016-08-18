get_filename_component(PLUGIN ${CMAKE_CURRENT_LIST_DIR} NAME)

set(${PLUGIN}_plugin_dir ${PROJECT_SOURCE_DIR}/plugins/${PLUGIN})

add_python_style_test(
    python_static_analysis_${PLUGIN} "${${PLUGIN}_plugin_dir}/server"
    )

add_eslint_test(
    js_static_analysis_${PLUGIN} "${PROJECT_SOURCE_DIR}/plugins/${PLUGIN}/web_external/js"
    ESLINT_CONFIG_FILE "${PROJECT_SOURCE_DIR}/plugins/${PLUGIN}/.eslintrc"
    )

