## Story 01
* greet
    - utter_hello

* goodbye
    - utter_goodbye

## Story 02
* goodbye
    - utter_goodbye
    - export

## Story 03
* greet
    - utter_hello
    - export

## Generated Story -8537736732681661193
* greet
    - utter_hello
* inform
    - utter_ask_building
* directions
    - export


## Generated Story 6460753783067090419
* greet
    - utter_hello
* directions{"building": "administration"}
    - slot{"building": "administration"}
    - utter_confirm_building
* affirm
    - export

## Generated Story -4080981297232232460
* greet
    - utter_hello
* inform
    - utter_ask_building
* directions{"building": "faculty"}
    - slot{"building": "faculty"}
    - utter_confirm_building
* deny
    - utter_ask_building
* directions{"building": "administration"}
    - slot{"building": "administration"}
    - utter_confirm_building
* affirm
    - action_building_direction
    - export

## Generated Story -4262779924873087368
* greet
    - utter_hello
* inform
    - utter_ask_building
* directions{"building": "faculty of engineering"}
    - slot{"building": "faculty of engineering"}
    - utter_confirm_building
* affirm
    - action_building_direction
    - slot{"results": "[faculty_of_engineering]: Face left, blue roof building is the one you are looking for"}
* feedback
    - utter_thank_response
* goodbye
    - utter_goodbye
    - export

## Generated Story 2491461716377050658
* greet
    - utter_hello
* directions{"building": "dpt of chemical engineering"}
    - slot{"building": "dpt of chemical engineering"}
    - utter_confirm_building
* deny
    - utter_ask_building
* directions{"building": "clinic"}
    - slot{"building": "clinic"}
    - utter_confirm_building
* affirm
    - action_building_direction
    - slot{"results": "[clinic]: The building with a national flag only on top of it is the one"}
* feedback
    - utter_thank_response
* goodbye
    - utter_goodbye
    - export

## Generated Story 2440656892040991668
* greet
    - utter_hello
* directions{"building": "faculty of commerce"}
    - slot{"building": "faculty of commerce"}
    - utter_confirm_building
* affirm
    - action_building_direction
    - slot{"results": "[faculty of commerce]: Face left, blue roof building is the one you are looking for"}
* feedback
    - utter_thank_response
* goodbye
    - utter_goodbye
    - export

## Generated Story 8068114631415307576
* greet
    - utter_hello
* inform
    - utter_ask_building
* directions{"building": "administration"}
    - slot{"building": "administration"}
    - utter_confirm_building
* affirm
    - action_building_direction
    - slot{"results": "[administration]: Face left, blue roof building is the one you are looking for"}
* feedback
    - utter_thank_response
* goodbye
    - utter_goodbye
    - export
    - export
