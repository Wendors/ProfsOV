#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Розширений тест для додатку ProfsOV після міграції на PySide6
"""

import sys
import os
import tempfile
from PySide6 import QtWidgets, QtCore, QtGui

def test_main_app():
    """Тестування основного додатку"""
    try:
        # Navigate to project directory
        project_dir = "/home/wandors/MyCode/Python/ProfsOV"
        os.chdir(project_dir)
        sys.path.insert(0, project_dir)

        app = QtWidgets.QApplication.instance()
        if app is None:
            app = QtWidgets.QApplication(sys.argv)
        
        # Test import of main modules
        import Baza
        import WrData
        import FormNM
        import FormOBL
        import zvits
        import Profs_rc
        
        print("✓ Всі модулі імпортовано успішно")
        
        # Test creating main form
        from Baza import Ui_Form
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        
        # Test with default database path
        home_dir = os.path.expanduser("~")
        test_db_path = os.path.join(home_dir, "test_profile.dbs")
        
        try:
            ui.setupUi(Form, path=test_db_path)
            print("✓ Основна форма створена успішно")
        except Exception as e:
            print(f"✗ Помилка створення основної форми: {e}")
            return False
        
        # Test FormNM creation
        try:
            from FormNM import Ui_FormN
            FormNN = QtWidgets.QWidget()
            uiN = Ui_FormN()
            uiN.setupUi(FormNN)
            print("✓ Форма створення записів працює")
        except Exception as e:
            print(f"✗ Помилка форми створення записів: {e}")
            return False
        
        app.quit()
        return True
        
    except Exception as e:
        print(f"✗ Загальна помилка тестування: {e}")
        return False

def test_widgets_compatibility():
    """Тестування сумісності віджетів"""
    try:
        app = QtWidgets.QApplication.instance()
        if app is None:
            app = QtWidgets.QApplication(sys.argv)
            
        # Test QDesktopWidget replacement
        screen = QtWidgets.QApplication.primaryScreen()
        geometry = screen.geometry()
        print(f"✓ Новий API екрану: {geometry.width()}x{geometry.height()}")
        
        # Test QComboBox enum
        combo = QtWidgets.QComboBox()
        combo.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        print("✓ QComboBox enum працює")
        
        # Test QFont without setWeight
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        print("✓ QFont без setWeight() працює")
        
        return True
        
    except Exception as e:
        print(f"✗ Помилка тестування віджетів: {e}")
        return False

def main():
    """Головна функція"""
    print("=" * 60)
    print("Розширений тест міграції ProfsOV на PySide6")
    print("=" * 60)
    
    tests = [
        ("Сумісність віджетів", test_widgets_compatibility),
        ("Основний додаток", test_main_app),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n[{test_name}]")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} - ПРОЙДЕНО")
            else:
                failed += 1
                print(f"❌ {test_name} - НЕ ПРОЙДЕНО")
        except Exception as e:
            failed += 1
            print(f"❌ {test_name} - КРИТИЧНА ПОМИЛКА: {e}")
    
    print("\n" + "=" * 60)
    print(f"РЕЗУЛЬТАТИ: {passed} пройдено, {failed} провалено")
    
    if failed == 0:
        print("🎉 ВСІ ТЕСТИ ПРОЙДЕНО! Міграція повністю успішна.")
        return True
    else:
        print("⚠️  Є проблеми, потрібна додаткова робота.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)