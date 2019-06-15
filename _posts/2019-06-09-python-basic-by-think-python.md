---
layout: post
title: "Python Basic"
subtitle: "책 「씽크 파이썬」을 바탕으로 한 python basic 공부"
tags: [python]
---



### Chapter 4

메서드 (method): 객체와 연관되어 있고, 점 표기법으로 호출되는 함수.  
캡슐화 (encapsulation): 코드 조각을 함수로 감싼 것.  
일반화 (generalization): 함수를 보다 범용적 (general)하게 만드는 것.  
인터페이스 (interface): 함수를 어떻게 사용해야 하는지 요약하는 것.  
> 인자는 무엇인가? 함수는 무엇을 하나? 그리고 반환값은 무엇인가?  

리펙터링 (refactoring): 인터페이스를 개선하고 코드 재사용을 쉽게 하도록 프로그램을 재정리하는 과정.  
독스트링 (docstring): 이 함수를 사용하는 데 필요한 정보는 들어 있어야 한다. 각 인자는 함수 동작에 어떤 영향을 미치는지 등.

기초적인 계발 계획:  
1. 함수 정의도 없는 작은 프로그램 작성  
2. 프로그램이 동작하면 관련된 코드를 찾아내서 함수로 **캡슐화** 함.  
3. 함수에 적절한 인자를 추가하면서 **일반화** 함.  

### Chapter 8
문자열은 불변!
```
fruit = 'banana'
fruit[0] = 'a'
TypeError: 'str' object does not support item assignment
```
