/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode*__restrict l1, ListNode*__restrict l2) {
        ListNode* res = new ListNode();
        ListNode* result = res;
        bool carry = 0;

        for(;;)
        {
            if (l1) { res->val += l1->val; l1 = l1->next; }
            if (l2) { res->val += l2->val; l2 = l2->next; }

            carry = res->val / 10;

            if (!l1 && !l2 && !carry)
            {
                break;
            }

            res->val %= 10;
            res->next = new ListNode(carry);
            res = res->next;
        };

        return result;
    }
};
