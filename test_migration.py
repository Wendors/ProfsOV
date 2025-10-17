#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Тестовий скрипт для перевірки міграції на PySide6
"""

def test_imports():
    """Тестування всіх імпортів"""
    try:
        from PySide6 import QtCore, QtGui, QtWidgets
        print("✓ PySide6 QtCore, QtGui, QtWidgets - OK")
    except ImportError as e:
        print(f"✗ PySide6 основні модулі - FAILED: {e}")
        return False
    
    try:
        from PySide6 import QtPrintSupport
        print("✓ PySide6 QtPrintSupport - OK")
    except ImportError as e:
        print(f"✗ PySide6 QtPrintSupport - FAILED: {e}")
        return False
    
    try:
        import WrData
        print("✓ WrData - OK")
    except ImportError as e:
        print(f"✗ WrData - FAILED: {e}")
        return False
    
    try:
        import Profs_rc
        print("✓ Profs_rc - OK")
    except ImportError as e:
        print(f"✗ Profs_rc - FAILED: {e}")
        return False
    
    return True

def test_app_creation():
    """Тестування створення додатку"""
    try:
        from PySide6 import QtWidgets, QtGui
        import sys
        
        app = QtWidgets.QApplication(sys.argv)
        print("✓ Створення QApplication - OK")
        
        widget = QtWidgets.QWidget()
        widget.setWindowTitle("Test PySide6")
        print("✓ Створення QWidget - OK")
        
        # Тест нового API для екрану
        screen = QtWidgets.QApplication.primaryScreen()
        geometry = screen.geometry()
        print(f"✓ primaryScreen() API - OK ({geometry.width()}x{geometry.height()})")
        
        # Тест шрифтів
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        print("✓ Шрифти без setWeight() - OK")
        
        app.quit()
        return True
    except Exception as e:
        print(f"✗ Створення додатку - FAILED: {e}")
        return False

def test_paths():
    """Тестування роботи з шляхами"""
    import os
    import tempfile
    
    try:
        pathtemp = os.path.join(tempfile.gettempdir(), "Proftemp")
        print(f"✓ Створення шляху: {pathtemp}")
        
        home_dir = os.path.expanduser("~")
        db_path = os.path.join(home_dir, "Профоблік.dbs")
        print(f"✓ Домашній шлях: {db_path}")
        
        return True
    except Exception as e:
        print(f"✗ Тестування шляхів - FAILED: {e}")
        return False

def main():
    """Основна функція тестування"""
    print("=" * 50)
    print("Тестування міграції ProfsOV на PySide6")
    print("=" * 50)
    
    tests = [
        ("Імпорти", test_imports),
        ("Створення додатку", test_app_creation),
        ("Робота з шляхами", test_paths)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n[{test_name}]")
        if test_func():
            passed += 1
            print(f"✓ {test_name} - PASSED")
        else:
            failed += 1
            print(f"✗ {test_name} - FAILED")
    
    print("\n" + "=" * 50)
    print(f"Результати: {passed} пройдено, {failed} не пройдено")
    print("=" * 50)
    
    if failed == 0:
        print("🎉 Всі тести пройдено! Міграція успішна.")
        return True
    else:
        print("⚠️  Є проблеми, потрібна додаткова робота.")
        return False

if __name__ == "__main__":
    main()