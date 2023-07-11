#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer
 * @number: integer
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *prev;
	listint_t *temp;

	prev = NULL;
	ptr = *head;
	temp = malloc(sizeof(listint_t));
	temp->n = number;
	while (ptr != NULL && ptr->n < number)
	{
		prev = ptr;
		ptr = ptr->next;
	}
	if (prev == NULL)
	{
		*head = temp;
		temp->next = ptr;
	}
	prev->next = temp;
	temp->next = ptr;
	return (ptr);
}
