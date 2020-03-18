#include <iostream>
#include <string>
#include <ctime>

using namespace std;

#define arr_len(arr) (sizeof(arr) / sizeof(*arr)); 

const int WIDTH = 2;
const int HEIGHT = 20;
const int WORD_LEN = 4;
const int DIFFICULTY = 4;
//const int DIFFICULT_WORD_LEN ?

int all_r[WIDTH][HEIGHT];

string symbols[] = {"`", "{", "}", "@", "+", "/", "|", "=", "^", "(", ")", "%", "'", "?", ".", "[", "]", ">", "<", ";", "_", "-", ",", "#", "$", "*"};
string words4[] = {"pack", "pawn", "pump", "peak", "wait", "half", "hour", "wave", "tent", "slot", "cast", "fuel", "last", "even", "gain", "east", "stab", "test", "seem", "mile", "lost", "ruin", "fade", "camp", "city", "joke", "bang", "nail", "hero", "halt", "sofa", "crew", "coin", "bait", "huge", "trip", "baby", "game", "film", "west", "wire", "hill", "help", "coup", "fish", "load", "tire", "form", "area", "swim"};

int words4_len = arr_len(words4);
int symbols_len = arr_len(symbols);


string gen_symbols(int iter) {
	int r;
	string rand_symbols;

	for (int i=0; i < iter; i++) {
		r = rand() % symbols_len;
		rand_symbols += symbols[r];
	}
	return rand_symbols;
}

string gen_screen() {
	int r, h;
	string screen;
	
	srand(time(NULL));
	int prefix = (rand() / 50);

	for (int n=0; n < HEIGHT; n++) {
		for (int i=0; i < WIDTH; i++) {
			r = rand() % words4_len;
			h = rand() % 10;
			screen += "0x" + to_string(prefix) + " " + gen_symbols(h) + words4[r] + gen_symbols(16-h) + "    ";
			all_r[i][n] = r;
			prefix++;
		}
		screen += '\n';
	}

	return screen;
}

int main() {
	int attempt_count = (WIDTH*HEIGHT)/DIFFICULTY;
	string screen = gen_screen();
	string inp;

	//get correct answer
	int magic_index_1 = rand() % WIDTH;
	int magic_index_2 = rand() % HEIGHT;
	int magic_index = all_r[magic_index_1][magic_index_2];
	string answer = words4[magic_index];

	while (attempt_count) { 
		int likeness = 0;
		/*string attemps;
		//Win only/ encoding problems on WSL
		for (int i=0; i<attempt_count; i++) {
			attemps += (char)219;
			attemps += " ";
		}
		*/
		#ifdef _WIN
			system("cls")
		#else
			system("clear");
		#endif

		cout << "Terminal\nPassword Required\nAttempts Remaining: " << to_string(attempt_count) << endl << screen << inp << endl;

		#ifdef DEBUG
			if (!inp.compare("~")) {
				cout << magic_index_1 << " " << magic_index_2 << " " << magic_index << endl;
				cout << answer << endl;
			} else if (!inp.compare("++")) {
				attempt_count += 10;
			}
		#endif

		for (int i=0; i<WORD_LEN; i++) {
			if (answer[i] == inp[i]) {
				likeness += 1;
			}
		}

		if (likeness==WORD_LEN) {
			cout << "Correct!" << endl;
			exit(0);
		}

		cout << "likeness: " << likeness << endl << ">";
		cin >> inp;

		attempt_count--;
	}

	cout << "[END]" << endl;
	return 0;
}