if(NOT DEFINED SRC_DIR)
    message(FATAL_ERROR "SRC_DIR is not defined.")
endif()
if(NOT DEFINED DST_DIR)
    message(FATAL_ERROR "DST_DIR is not defined.")
endif()

message(STATUS "Compiling UIs files...")
file(GLOB_RECURSE ui_files ${SRC_DIR}/*.ui)
foreach (ui_file ${ui_files})
    get_filename_component(ui_filename ${ui_file} NAME_WE)
    message(STATUS "uic ${ui_file} -o ${DST_DIR}/${ui_filename}.py -g python")
    execute_process(COMMAND uic ${ui_file} -o ${DST_DIR}/${ui_filename}_ui.py -g python)
endforeach()
message(STATUS "UI files compiled.")