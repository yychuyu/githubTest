bool isPalindrome(struct ListNode* head) {
        struct ListNode *point1, *point2, *point3;
        point3 = point2 = head;
        point1 = NULL;
        long int sum = 0;
        int n = 1;
        if(head == NULL || head->next == NULL)
            return true;
        while(point3->next != NULL)//��һ�α�����ȡֵ������
        {
            sum += n*point3->value;
            n++;
            point3 = point3->next;
            point2->next = point1; //�������һ���ڵ��ÿգ���Ϊ���ú��һ����������һ��
            point1 = point2;
            point2 = point3;
        }
        sum += n*point3->value;
        point2->next = point1;
        n = 1;
        while(point2 != NULL)//�ڶ��α���
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