#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i = 0;
	PyObject *obj;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
