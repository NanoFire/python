#include <windows.h>
#include <iostream>
using namespace std;

void click(int x, int y) {
    SetCursorPos(x, y);
    mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
    Sleep(100);  // Sleep for 100 milliseconds (equivalent to time.sleep(0.1) in Python)
    mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);
}

int main() {
    while (!GetAsyncKeyState('Q') & 0x8000) {
        COLORREF pixelColor = GetPixel(GetDC(NULL), 1000, 500);
        int r = GetRValue(pixelColor);
        int g = GetGValue(pixelColor);
        int b = GetBValue(pixelColor);
        
        if (r == 75 && g == 219 && b == 106) {
            click(1000, 500);
        }
    }

    return 0;
}