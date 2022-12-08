#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks to see if a linked list is palindrome
 * @head: head of the given linked list
 * Return: 1 if palindrom and 0 if not
 */
int is_palindrome(listint_t **head __attribute__((unused)))
{
	int n = 0;
	int m = 0;
	int i = 0;
	struct listint_s *current;
	int *tmp_ptr;

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	tmp_ptr = malloc(sizeof(int) * n);
	current = *head;
	while (current != NULL)
	{
		tmp_ptr[i] = current->n;
		current = current->next;
		i++;
	}

	while (m < (n / 2))
	{
		if (tmp_ptr[m] != tmp_ptr[n - m])
			return (0);

		printf("-- %d\n", tmp_ptr[m]);
		/*printf("m - %d | n/2 - %d | ->n %d\n", m, (n / 2), tmp_ptr[--i]);*/
		m++;
	}
	return (1);
}
