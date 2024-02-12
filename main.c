#include <stdio.h>

int main() {
    int taille = 6;
                       /*A, B, C, D, E, F*/
    int matrice[][6] = {{0, 1, 0, 0, 0, 0},
                        {1, 0, 1, 1, 0, 0},
                        {0, 1, 0, 0, 0, 0},
                        {0, 1, 0, 0, 1, 1},
                        {0, 0, 0, 1, 0, 0},
                        {0, 0, 0, 1, 0, 0}
    };

    int taillemaxchaine = taille - 1;
    printf("Taille maximal des chaines a tester (taille max est %d): \n", taille);
    scanf("%d", &taillemaxchaine);

    int i;
    int x;
    for (i = 1; i <= taillemaxchaine; i++) {
        for (x = 0; x <= i; x++) {

        }
    }

    return 0;
}

int chaine_exist(int* matrice[][6], int first, int second) {
    if (matrice[first][second])! {
        
    }
}

