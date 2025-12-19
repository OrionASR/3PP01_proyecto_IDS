section .data
    mensaje db 'Hola mundo', 10
    longitud equ $ - mensaje

section .text
    global _start

_start:
    mov eax, 4          ; sys_write
    mov ebx, 1          ; salida estándar (stdout)
    mov ecx, mensaje    ; dirección del mensaje
    mov edx, longitud   ; longitud del mensaje
    int 0x80            ; llamada al sistema

    mov eax, 1          ; sys_exit
    mov ebx, 0          ; código de salida
    int 0x80
