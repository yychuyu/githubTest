bool isPalindrome(struct ListNode* head) {
        struct ListNode *point1, *point2, *point3;
        point3 = point2 = head;
        point1 = NULL;
        long int sum = 0;
        int n = 1;
        if(head == NULL || head->next == NULL)
            return true;
        while(point3->next != NULL)//第一次遍历，取值并逆置
        {
            sum += n*point3->value;
            n++;
            point3 = point3->next;
            point2->next = point1; //将链表第一个节点置空，因为倒置后第一个变成了最后一个
            point1 = point2;
            point2 = point3;
        }
        sum += n*point3->value;
        point2->next = point1;
        n = 1;
        while(point2 != NULL)//第二次遍历
        {
            sum -= n*point2->value;
            n++;
            point2 = point2->next;
        }
        if(sum == 0)
            return true;
        else
            return false;
    }