/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    
    // Steps to solving this problem
    // Step 1: Create copy of both nodes and calculate the length of each node
    // Logic: It is safe to assume that if the 2 nodes are of different length, any values before the index of the difference will not be the interesction point.
    // Step 2: Based on which has the longer length, move the nodes length number of times to skip the redundant values to save on run time.
    // Step 3: Compare the values of following node to find the proper intersection point, returning either of the 2 nodes as both points to the intersection point.
    
    struct ListNode *nodeA = headA;
    struct ListNode *nodeB = headB;
    
    int A = 0, B = 0;
    int diff = 0;
    
    while (nodeA != NULL){
        A++;
        nodeA = nodeA->next;
    }
    
    while (nodeB != NULL){
        B++;
        nodeB = nodeB->next;
    }
    
    if (A < B){
        diff = B - A;
    }
    else{
        diff = A - B;
    }
    
    nodeA = headA;
    nodeB = headB;
    int count = 0;
    
    while (count < diff){
        if (A < B){
            nodeB = nodeB->next;
        }
        else{
            nodeA = nodeA->next;
        }
        count++;
    }
    
    while (nodeA != NULL){
        if (nodeA == nodeB){
            return nodeA;
        }
        nodeA = nodeA->next;
        nodeB = nodeB->next;
    }
    return NULL;
}