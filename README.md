# Google Mapper Documentation
#### Objective
To provide a full stack application for choosing and storing addresses from Google maps into database and fusion tables.

#### Approach
Integrate a Django standalone project and application.

###### Expected Use cases
![alt text](https://github.com/renatosamperio/mapping_app/blob/master/doc/Use%20Cases.png "Use Cases"){ width=75% }
The main use cases are:
 - Choose locations in Google Map
 - Store locations in DB and Fusion Tables
 - Clear locations

###### Information flow
![alt text](https://github.com/renatosamperio/mapping_app/blob/master/doc/Data%20Flow%20Diagram.png "Data flow")
The data flows is represented as follows:
1. User collects interes points on the map. At this point, they are not yet map markers
2. Application converts interest points into valid addresses
3. Application displays only valid addresses of clicked interested points as a map marker
4. Application sends valid google addresses into a database in backe end

###### Information sequence
![alt text](https://github.com/renatosamperio/mapping_app/blob/master/doc/Sequence%20Diagram.png "Sequence Diagram")

The communication between components is show in previous diagram. 