#include<stdio.h>

void Torre();
void Alfil();

int main()
{
    int opcion=0;

    while(1)
    {
        printf("\n\t***Movimientos válidos en piezas de ajedrez***\n");
        printf("\n¿Qué desea realizar?\n");
        printf("\n1 Alfil.\n");
        printf("2 Torre.\n");
        printf("3 Salir.\n");
        printf("\nIngrese una opción: ");
        scanf("%d", &opcion);
        
        switch(opcion)
        {
            case 1:
            Alfil();
            break;
            case 2:
            Torre();
            break;
            case 3:
            return 0;
            default:
            printf("Opción no válida.\n");
        }

    }

    return 0;
}

void Alfil()
{
    int x, y, i, j; 
    int tablero[8][8]; 
    
    printf("\nIngrese x: ");
    scanf("%d",&x);
    printf("Ingrese y: ");
    scanf("%d",&y);

    // cerar toda la matriz 

    for (i=0; i<8; i++)
    {
        
        for (j=0; j<8; j++)
        { 
            tablero[i][j]=0; 
        
        }
    }
    
    // cargar las posiciones por la que puede pasar el alfil //
    
    for (i=x, j=y; (i<8&&j>=0); i++, j--) // valida que el contador no pase los limites del tablero//
    {
        if (x+y == i+j) // valida que sea la diagonal que corresponde a x,y.//
        {
            tablero[i][j]=1;
        }
    }
    
    for (i=x, j=y; (i>=0&&j<8); i--, j++)
    {
        if (x+y == i+j)
        {
            tablero[i][j]=1;
        } 
    }
    
    for (i=x, j=y; (i<8||j<=0); i++, j++)
    {
        if (i>x&&j>y)
        {
            tablero[i][j]=1; 
        }  
    } 
    
    for (i=x, j=y; (i>=0&&j>=0); i--, j--)
    {
        if (i<x&&j<y)
        {
            tablero[i][j]=1; 
        }  
    } 
  

    tablero[x][y]=7; // la posicion del alfil 
    
    //  impresion del tablero de ajedrez //
    
    printf("\n \n \t \t \t \t LAS COORDENADAS DEL ALFIL SON: (x:%d, y:%d) \n \n \n",x,y);
    
    for (j = 7; j >= 0; j--){ 
        
        if (i != 0 ) printf("%d", j); //imprime valores en Y
        
        for (i = 0; i < 8; i++)
        { 
            if (j == 0) printf(" %d ", i); //imprime valores en X
            
            if(tablero[i][j]==0) printf("*\t"); 
         
            if(tablero[i][j]==1) printf("X\t");
            
            if(tablero[i][j]==7) printf("A\t");
        
        } 
        
        printf("\n\n"); 
    }  
}

void Torre()
{
    int x, y, i, j; 
    int tablero[8][8]; 
    
    printf("\nIngrese x: ");
    scanf("%d",&x);
    printf("Ingrese y: ");
    scanf("%d",&y);
    
    // cerar toda la matriz 

    for (i=0; i<8; i++)
    {
        
        for (j=0; j<8; j++)
        { 
            tablero[i][j]=0; 
        
        }
    }
    
    tablero[x][y]=7; // la posicion de la torre
    
    //  impresion del tablero de ajedrez //
    
    printf("\n \n \t \t \t \t LAS COORDENADAS DE LA TORRE SON: (x:%d, y:%d) \n \n \n",x,y);
    
    for (j = 7; j >= 0; j--){ 
        
        if (i != 0 ) printf("%d", j); //imprime valores en Y
        
        for (i = 0; i < 8; i++)
        { 
            if (j == 0) printf(" %d ", i); //imprime valores en X
            
            if(tablero[i][j]==0) printf("*\t"); 
         
            if(tablero[i][j]==1) printf("X\t");
            
            if(tablero[i][j]==7) printf("T\t");
        
        } 
        
        printf("\n\n");
    } 

}