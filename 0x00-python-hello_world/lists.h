#ifndef LIST_H
#define LIST_H

/**
 * listint_s - singly linked list
 * @n: the integer
 * @next: pointer to next node
 *
 * Description: Singly linked node structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

int check_cycle(listint_t *list);

#endif
