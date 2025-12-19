#include <stdio.h>
#include <string.h>
#include <conio.h>

#define MAX 100
#define MAXALUMS 10
#define BAR 60

//Prototipos
void menu();
void barrita(int cantidad);
void registrarAlumno();
void mostrarAlumnos();
void buscarAlumno(int calificacion);
void ordenarAlumnos();


//LA ESTRUCTURA!

struct Alumno {
	char nombre[MAX];
	char apPat[MAX];
	char apMat[MAX];
	int edad;
	float calificacion;
} alumnos[MAXALUMS];

int totalAlumnos = 0;

//El main we
int main() {
	float calificacion = 0;
	char opcion = '\0';
	int tecla = 0;
	
	do {
		barrita(BAR);
		menu();
		opcion = getche();
		
		do {
			tecla = getch();
		} while (tecla != 13);
		
		barrita(BAR);
		switch(opcion) {
			case '1':
				registrarAlumno();
				break;
			
			case '2':
				mostrarAlumnos();
				break;
			
			case '3':
				printf("Ingresa la calificacion del alumno que estes buscando: ");
				scanf("%f",&calificacion);
				buscarAlumno(calificacion);
				break;
				
			case '4':
				ordenarAlumnos();
				break;
			
			case '9':
				printf("Gracias por usar mi programa, vuelve pronto!");
				barrita(BAR);
				break;
			
			default:
				printf("Opcion invalida o desconocida. Intentalo de nuevo.");
		}
		
	} while (opcion != '9');
	
	return 57;
}

//Las funciones we
void menu() {
	printf("======/ MENU \\======\
			\n1. Registrar alumno\
			\n2. Mostrar todos los alumnos\
			\n3. Buscar alumno (por calificacion)\
			\n4. Ordenar alumnos (por calificacion)\
			\n9. Salir\
			\n	Elige una opcion: ");
}

void barrita(int cantidad) {
	printf("\n\n+");
	for (int i = 0; i < cantidad; i++) {
		printf("-");
	}
	printf("+\n\n");
}

void registrarAlumno() {
	int tecla = 0;
	
	do {
		printf("\nIngrese nombre(s) del alumno: ");
		scanf(" %[^\n]", alumnos[totalAlumnos].nombre);
		
		printf("Ingrese el apellido paterno del alumno: ");
		scanf(" %[^\n]", alumnos[totalAlumnos].apPat);
		
		printf("Ingrese el apellido materno del alumno: ");
		scanf(" %[^\n]", alumnos[totalAlumnos].apMat);
		
		printf("Ingrese la edad del alumno: ");
		scanf("%d",&alumnos[totalAlumnos].edad);
		
		printf("Ingrese la calificacion del alumno: ");
		scanf("%f",&alumnos[totalAlumnos].calificacion);
		
		totalAlumnos++;
		printf("\nAlumno registrado!!\n");
		
		printf("Presiona 'Enter' para registrar otro alumno o cualquier tecla para salir\n");
		tecla = getch();
	} while (tecla == 13);
}

void mostrarAlumnos() {
	printf("\n-----+ Lista de Alumnos +-----");
	for (int i = 0; i < totalAlumnos; i++) {
		printf("\n | Nombre completo: %s %s %s | Edad: %d | Calificacion: %.2f",
				alumnos[i].nombre, alumnos[i].apPat, alumnos[i].apMat, alumnos[i].edad, alumnos[i].calificacion);
	}
}

void buscarAlumno(int calificacion) {
	bool encontrado = false;
	
	for (int i = 0; i < totalAlumnos; i++) {
		if (alumnos[i].calificacion == calificacion) {
			encontrado = true;
			
			printf("\nAlumno(s) encontrado(s)!!");
			printf("\n | Nombre completo: %s %s %s  | Edad: %d | Calificacion: %.2f",
					alumnos[i].nombre, alumnos[i].apPat, alumnos[i].apMat, alumnos[i].edad, alumnos[i].calificacion);
		}
	}
	
	if (!encontrado) {
		printf("\nAlumno(s) no encontrado(s). Intentalo de nuevo.");
	}
}

void ordenarAlumnos() {
	Alumno alumnoTMP;
	
	for (int i = 0; i < totalAlumnos; i++) {
		for (int j = 0; j < totalAlumnos - 1; j++) {
			if (alumnos[j].calificacion < alumnos[j + 1].calificacion) {
				alumnoTMP = alumnos[j];
				alumnos[j] = alumnos[j + 1];
				alumnos[j + 1] = alumnoTMP;
			}
		}
	}

	for (int l = 0; l < totalAlumnos; l++) {
		printf("\n | Nombre completo: %s %s %s  | Edad: %d | Calificacion: %.2f",
				alumnos[l].nombre, alumnos[l].apPat, alumnos[l].apMat, alumnos[l].edad, alumnos[l].calificacion);
		
	}
}
