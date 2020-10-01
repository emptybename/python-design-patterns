# What is System Architecture Design
System Architecture Design is a conceptual representation of the components and subcomponents that reflects the 
behaviour of a system.

System architects or solution architects are the people who know what components to choose for the specific use case,


Today you are going to learn the basic components that are necessary to get started with system architecting. 
And principles to keep in mind while designing such systems.

## Basic concepts
    - Latency
    - Throughput
    - Bandwidth
    - Vertical Scaling, Horizontal Scaling, Auto Scaling

These are the basic concepts you need to know to get started with system architecture

### Latency, Throughput, Bandwidth
A better way to understand latency and throughput is imagining a bunch of cars moving from point A(source) to point 
B(destination) through an expressway.

### Latency
- The time taken for any given car to travel from source to destination is the latency experienced by that car. 
- Latency is always the unit of time

### Bandwidth
- The maximum number of vehicles that can travel through the expressway is called bandwidth
- Let’s say maximum 4 vehicles can go through the expressway. Then the bandwidth of this expressway is 4 vehicles/hour

### Throughput
- The actual number of vehicles that can travel through the expressway at any given condition (irrespective of 
its maximum bandwidth) is called throughput.
- E.g 
    - At any given time due to traffic or some other reasons, the number of vehicles travelling through the 
    expressway reduces. Let’s say it usually get reduced to 3 vehicles/hour at peak hours then throughput is 3 v/h

```
One should keep in mind that increasing the bandwidth affects the throughput but may not necessarily help to 
reduce the latency
```
### Vertical Scaling, Horizontal Scaling and Auto Scaling
To understand this lets take one scenario

Now we got some requirement that we need to accommodate more vehicles in our expressway.

Let say earlier we had 2 lane expressway. How to fulfil this requirement.

- By increasing the bandwidth.
- E.g
    - We will do this by scaling our existing expressway to 3 lanes. Now it can accommodate maximum 8 vehicles/hour

Since our expressway’s bandwidth has been increased to 8 vehicles/hour. At peak hours the throughput 
becomes 7 vehicles/hour. 

Even though the throughput is better now, it does not necessarily reduce the time taken by a car to get to its 
destination. Some cars still might experience latency because of their maximum cruising speed or patchy roads in their 
lane or sometimes even a slow driver.

When it comes to computer systems, you can assume the cars are the data packets and expressway is our channel or system. 
The bandwidth or throughput is measured in bits/s or Mbits/s.

If you notice you just scaled the expressway by adding more lanes to the existing one. Doing this might disturb the 
traffic in the expressway but it scales in this scenario. 


### Vertical Scaling 
In computer systems, When you scale vertically you add more resources like CPU, RAM and SSD to the existing machine.
This is called vertical scaling.

You can also scale the expressway without disturbing the existing traffic. 
This can be done by building another parallel expressway.

### Horizontal Scaling
In system architectures, you add more machines by just replicating them to increase the throughput of the overall system.

Now imagine, you somehow have the ability to build and destroy an expressway instantly. During peak times in order to 
increase the throughput, you can replicate the expressways (horizontally scale) based on the traffic. Then when traffic 
returns to normal you can destroy the extra expressways. This is nothing but auto-scaling.

### Auto Scaling
In computer systems, based on the load experienced by our system we do auto-scaling by replicating the machines. 
When load reduces we remove the machines that are idle.

## Basic components
System design involves assembling the right components to solve the problem at hand. There are thousands of components 
or stacks available from different cloud providers. But worry not, you don’t have to know all those to build a simple 
architecture.

```
Virtual Machine
Load Balancer
Database
Cache
```







