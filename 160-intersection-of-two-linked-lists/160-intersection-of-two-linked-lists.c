/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include <string.h>

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
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