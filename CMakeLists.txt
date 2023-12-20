cmake_minimum_required(VERSION 3.14)

project($ENV{REZ_BUILD_PROJECT_NAME} NONE)

# Install python files
install(DIRECTORY $ENV{REZ_BUILD_SOURCE_PATH}/python DESTINATION ${CMAKE_INSTALL_PREFIX})

# Compile .ui to .py
install(
    CODE
    "execute_process(COMMAND ${CMAKE_COMMAND} -DSRC_DIR='$ENV{REZ_BUILD_SOURCE_PATH}/resources/ui' -DDST_DIR='$ENV{REZ_BUILD_INSTALL_PATH}/python/$ENV{REZ_BUILD_PROJECT_NAME}/ui' -P $ENV{REZ_BUILD_SOURCE_PATH}/cmake/compileUiHelper.cmake)"
    COMPONENT Runtime
)
