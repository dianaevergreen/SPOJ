#include &lt;iostream&gt;
using namespace std;

#define MAXR 100
#define MAXC 100

int max(int arreglete[MAXC], int cant)
{   int ma = arreglete[0];
    for(int x = 0; x&lt;cant; x++)
    {
        if (ma &lt;= arreglete[x])
        {
            ma = arreglete[x];  
           
        }

    } 
    return ma;    
}


int max_dos(int g, int h)
{
    if(g &gt; h)
    {
        return g;

    }   
    else
    {
        return h;
    }
}


int max_tres(int e, int y, int u)
{
   int mu[3] = {e,y,u};
    int me = 0;

    for(int o = 0; o &lt;3; o++)
    {
        if (me &lt; mu[o])
        {me = mu[o];}
    }
   return me;
}



int path(int m[][MAXC], int r, int c)
{int array [r][c];
    
    for(int a = r-1; a &gt;= 0; a--)
    {        
        for (int b = 0; b &lt; c; b++)
        {
            if (a == r-1)
            {
               array[a][b] = m[a][b];
               
               
            }

            else if(b == 0)
            {
                array[a][b] = max_dos(m[a][b] + array[a+1][b], m[a][b] + array[a+1][b+1]);
                
                
            }

            else if(b == c-1)
            {
                array[a][b] = max_dos(m[a][b] + array[a+1][b-1], m[a][b]+array[a+1][b]);
                
            }

            else
                array[a][b] = max_tres(m[a][b] + array[a+1][b-1], m[a][b] + array[a+1][b], m[a][b] + array[a+1][b+1]);
                
            }
            
        }

int mayor = 0;
for (int l =0; l &lt; r; l++)
{
    for (int j =0; j&lt;c; j++)
    {
        if (mayor &lt; array[l][j])
        {
            mayor = array[l][j];
        }
    }

  
}

return mayor;
    }

    
//int mayor =  max(array,c); 

//return 0; //mayor;
//}



int deuno(int m[][MAXC],int r)
{
    int resp = 0;

    for (int uno = 0; uno &lt; r; uno++)
    {
        resp += m[uno][0];
            
    }
    return resp;   
}



int main(){

int cases, row, col, stones;

cin &gt;&gt; cases;

for(int i = 0; i &lt; cases; i++)
    {
        cin &gt;&gt; row &gt;&gt; col ;
        
        if ((row == 0)||(col == 0))
        {
            cout &lt;&lt;0&lt;&lt;"\n";
            continue;
        }
        int matrix [MAXR][MAXC];
       

        for (int j = 0; j &lt; row; j++)
        {
            for (int k = 0; k &lt; col; k++)
            {
                cin &gt;&gt; matrix[j][k];
                
            }

        }

        if (col == 1)
        {
            stones = deuno(matrix, row);
            cout &lt;&lt; stones &lt;&lt;"\n";
        }

        else
        {
            int biggerpath = path(matrix, row, col); 
            
            cout &lt;&lt; biggerpath&lt;&lt;"\n";          
        }
        
        
    }
}





