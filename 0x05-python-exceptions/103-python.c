#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - function to print
 * information about a Python list object
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Error: Object is not a Python list\n");
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
}

/**
 * print_python_bytes - function to print
 * information about a Python bytes object
 * @p: Python Object
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Error: Object is not a Python bytes object\n");
		return;
	}
	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python bytes object = %lu\n", PyBytes_Size(p));
	printf("[*] First %d bytes:", PyBytes_Size(p) > 10 ? 10 : PyBytes_Size(p));
	for (unsigned char i = 0; i < PyBytes_Size(p) && i < 10; i++)
		printf(" %02x", (unsigned char)PyBytes_AsString(p)[i]);
	printf("\n");
}

/**
 * print_python_float - function to print
 * information about a Python float object
 * @p: Python Object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("Error: Object is not a Python float object\n");
		return;
	}
	printf("[*] Python float info\n");
	printf("[*] Float value: %.16g\n", PyFloat_AsDouble(p));
}

