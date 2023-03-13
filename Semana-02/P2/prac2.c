#include<stdio.h>

#define TAM_FIL 8
#define TAM_COL 8
 
int tablero[TAM_FIL][TAM_COL];

void Reina(int *x, int *y);
void Rey(int *x, int *y);
 
int main(){
    
    int opcion = 0;
    int x[TAM_FIL];
    int y[TAM_COL];
    
    while (1){
        
        printf("\n\t***Movimientos válidos en piezas de ajedrez***\n");        
        printf("\n¿Qué desea realizar?\n");
        printf("\n1) Reina\n");
        printf("2) Rey\n");
        printf("3) Salir.\n");
        printf("\nIngrese una opción: ");
        scanf("%d", &opcion);
        
        switch(opcion)
        {
            case 1:
            printf("\nIngrese la posicion de la Reina en este formato -> x,y: ") ; 
            scanf("%d , %d", x, y); 
            Reina( x , y);
            break;
            case 2:
            printf("\nIngrese la posicion del Rey en este formato -> x,y: ") ; 
            scanf("%d , %d", x, y); 
             Rey( x , y);
             break;
             case 3:
             return 0;
             default:
             printf("\nOpción no valida");
        }
    }
    
    return 0; 

}

//**************************************************************************************************************************//

void Reina(int *x, int *y)
{
    int  i, j; 

    // cerar toda la matriz 

    for (i=0; i<8; i++)
    {
        
        for (j=0; j<8; j++)
        { 
            tablero[i][j]=0; 
        
        }
    }
    
//--------------------- cargar las posiciones por la que puede pasar la torre ------------------------------//
    
//---------------------------------Posición 1---------------------------------------------//  
    
    for (i = *x, j = *y ; ( i < 8 && j >= 0); i++, j--) // valida que el contador no pase los limites del tablero//
    {
        if (*x + *y == i+j) // valida que sea la diagonal que corresponde a x,y.//
        {
            tablero[i][j]=1;
        }
    }

//---------------------------------Posición 2---------------------------------------------//    

    for (i = *x , j = *y ; ( i >= 0 && j < 8); i--, j++)
    {
        if (*x + *y == i+j)
        {
            tablero[i][j]=1;
        } 
    }
    
//---------------------------------Posición 3---------------------------------------------//    

    for ( i = *x , j = *y ; ( i < 8 || j <= 0); i++, j++)
    {
        if ( i > *x && j > *y)
        {
            tablero[i][j]=1; 
        }  
    } 

//---------------------------------Posición 4---------------------------------------------//    
    
    for (i = *x , j = *y ; ( i >= 0 && j >= 0); i--, j--)
    {
        if (i < *x && j < *y)
        {
            tablero[i][j]=1; 
        }  
    }
    
//---------------------------------Posición 5---------------------------------------------//    
    
    for ( i = *x ; i < 0 ; i++) // valida que el contador no pase los limites del tablero//      
    {                                                                                     
            tablero[i][j]=1;                                                              
    }                                                                                     
    for (j = *y ; j < 8 ; j++) // valida que el contador no pase los limites del tablero//
    {
            tablero[i][j]=1;
        
    }
//---------------------------------Posición 6---------------------------------------------//    
    
    for (i = *x ; i > 8 ; i--)      
    {                                                                                     
            tablero[i][j]=1;                                                              
    }                                                                                     
    for (j = *y ; j >= 0 ; j--)
    {
            tablero[i][j]=1;
        
    }
    
//---------------------------------Posición 7---------------------------------------------//    

    for (j = *y ; j <= 0 ; j++)
    {
        tablero[i][j]=1; 
    }

//---------------------------------Posición 8---------------------------------------------//    
    for (i = *x ; i >= 0 ; i--)
    {
        tablero[i][j]=1; // X X X T
    } 

    for (i = *x ; i < 8 ; i++)
    {
        tablero[i][j]=1; // T X X X
    } 


//---------------------------------------------------------------------------------------------//

    tablero[*x][*y]=7; // la posicion de la Reina
    
    printf("\n \n \t \t \t \t LAS COORDENADAS DE LA REINA SON: (x:%d, y:%d) \n \n \n", *x, *y);
    
//-----------------------------impresion del tablero de ajedrez------------------------------------------//
    
    for (j = 7 ; j >= 0 ; j--){ 
        
        if (i != 0 ) printf("%d", j); //imprime valores en Y
        
        for (i = 0 ; i < 8 ; i++)
        { 
            if (j == 0) printf(" %d ", i); //imprime valores en X
            
            if(tablero[i][j]==0) printf("*\t"); 
         
            if(tablero[i][j]==1) printf("X\t");
            
            if(tablero[i][j]==7) printf("Q\t");
        
        } 
        
        printf("\n\n"); 
    }  
}

//*****************************************************************************************************************************//

void Rey(int *x , int *y)
{
    int  i, j; 

    // cerar toda la matriz 

    for (i=0; i<8; i++)
    {
        
        for (j=0; j<8; j++)
        { 
            tablero[i][j]=0; 
        
        }
    }
    
//--------------------- cargar las posiciones por la que puede pasar el rey ------------------------------//
    
//---------------------------------Posición 1---------------------------------------------//  

    int i1 = *x-1;
    int j1 = *y-1;

    if ( i1<8 && j1<8 )
    {
        tablero[i1][j1]=1;
        i1--;
        j1--;
    }

//---------------------------------Posición 2---------------------------------------------//    

    int i2 = *x+1;
    int j2 = *y+1;

    if ( i2<8 && j2<8 )
    {
        tablero[i2][j2]=1;
        i2++;
        j2++;
    }
   
//---------------------------------Posición 3---------------------------------------------//    

    int i3 = *x-1;        
    int j3 = *y+1;

    if ( i3<8 && j3>0 )
    {
        tablero[i3][j3]=1;            //problema
        i3--;
        j3++;
    }   

//---------------------------------Posición 4---------------------------------------------//    
   
    int i4 = *x+1;
    int j4 = *y-1;

    if ( i4>0 && j4<8 )
    {
        tablero[i4][j4]=1;
        i4++;
        j4--;
    } 
   
//---------------------------------Posición 5---------------------------------------------//    
    
    int i5 = *x;        
    int j5 = *y+1;
    
    if (i5<8)   
    {
        tablero[i5][j5]=1; 
    }                                                                                     
    if (j5<8)                   //problema
    {
        tablero[i5][j5]=1;
        j5++;
    }
    
//---------------------------------Posición 6---------------------------------------------//    
    
    int i6 = *x;
    int j6 = *y-1;
    
    if (i6<8)   
    {
        tablero[i6][j6]=1; 
    }                                                                                     
    if (j6>8) 
    {
        tablero[i6][j6]=1;
        j6--;
    }
   
//---------------------------------Posición 7---------------------------------------------//    

    int i7 = *x+1;
    int j7 = *y;
    
    if (i7>0)   
    {
        tablero[i7][j7]=1; 
        i7++;
    }                                                                                     
    if (j7<0)                
    {
        tablero[i7][j7]=1;
    }
//---------------------------------Posición 8---------------------------------------------//    
    int i8 = *x-1;
    int j8 = *y;
    
   if (i8>0)   
    {
        tablero[i8][j8]=1; 
        i8++;
    }                                                                                     
    if (j8<8) 
    {
        tablero[i8][j8]=1;
    }
    
//-------------------------------------------------------------------------------------------------------//
    
    tablero[*x][*y]=7; // la posicion del Rey
    
    printf("\n \n \t \t \t \t LAS COORDENADAS DEL REY SON: (x:%d, y:%d) \n \n \n", *x, *y);
    
//-----------------------------impresion del tablero de ajedrez------------------------------------------//
    
    for (j = 7; j > 0; j--){ 
        
        if (i != 0 ) printf("%d", j); //imprime valores en Y
        
        for (i = 0; i < 8; i++)
        { 
            if (j == 0) printf(" %d ", i); //imprime valores en X
            
            if(tablero[i][j]==0) printf("*\t"); 
         
            if(tablero[i][j]==1) printf("X\t");
            
            if(tablero[i][j]==7) printf("R\t");
        
        } 
        
        printf("\n\n"); 
    } 
}