cmake_minimum_required(VERSION 2.8.3)
project(image_recognition_tensorflow)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()


if (CATKIN_ENABLE_TESTING)
    # Test catkin lint
    find_program(CATKIN_LINT catkin_lint REQUIRED)
    execute_process(COMMAND "${CATKIN_LINT}" "-q" "-W2" "${CMAKE_SOURCE_DIR}" RESULT_VARIABLE lint_result)
    if(NOT ${lint_result} EQUAL 0)
      message(FATAL_ERROR "catkin_lint failed")
    endif()

    catkin_add_nosetests(test)
endif()

install(PROGRAMS
  scripts/evaluate_classifier
  scripts/get_object_recognition
  scripts/object_recognition_node
  scripts/retrain
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
