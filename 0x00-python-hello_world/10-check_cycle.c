#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle.
 * @list: list to check.
 * Return: 1/0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p, *fast_p;

	if (!list || list->next == NULL)
		return (0);

	slow_p = list->next;
	fast_p = list->next->next;

	while (slow_p && fast_p && fast_p->next)
	{
		if (slow_p == fast_p)
			return (1);

		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
	}

	return (0);
}
