# Load balancer

![database-python](https://i1.wp.com/gbhackers.com/wp-content/uploads/2018/12/Load-Balancer.jpg?w=759&ssl=1)

[Reference](https://gbhackers.com/load-balancer-reverse-proxy/)

---
Load Balancer basically helps to distribute the network traffic across the multiple servers to improve the network, application performance. the Reconnaissance work on target to find out target domain has a load balancer so that penetration testing does not misdirect your probs or attacks.

## Why are load balancer is useful?

-   Load Balancer acts as a  **reverse proxy**  which  **distributes**  application or network traffic across a number of servers.
-   It ensures  **reliability**  and  **availability**  by monitoring the health of the application and sending a request server or application that can respond in  **a timely**  manner.
-   Load balancers are found in the network and transport layer  **(IP, TCP, FTP, UDP**) and application layer  **(HTTP)**

### **Standard Industry algorithm:**

**Round-robin load balancing** is one of the simplest methods for distributing client requests across a group of servers. Going down the list of servers in the group, the round-robin load balancer forwards a client request to each server in turn.
-   Does not always result in the accurate or efficient distribution of traffic, because many  **round-robin load balancers**  assume that all servers are the same: currently up, currently handling the same load, and with the  **same storage and computing capacity.**
-   **Weighted round robin** – A weight is assigned to each server based on criteria chosen by the site administrator, most commonly used criterion is the  **server’s traffic-handling capacity.**
-   **Least Connections:** If two servers in a  **cluster**  have exactly the same specification, one server can still get overloaded considerably faster than the other.
-   **Random Connections:** load balancer receives a large number of requests, a  **Random algorithm**  will be able to distribute the requests evenly to the nodes.

---