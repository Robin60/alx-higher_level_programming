#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the linked list
 * @number: the value inserted
 * Return: address of new node, NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;

	return (new);
}
