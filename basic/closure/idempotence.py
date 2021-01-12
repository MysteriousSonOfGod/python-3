
# Idempotence 은 수학 및 컴퓨터 과학의 특정 연산의 속성으로, 초기 적용 이후 결과를 변경하지 않고 여러 번 적용 할 수 있습니다

# 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질
# 어떤 단항연산(또는 함수)은 어느 값에라도 두 번 적용되었을 때, 한 번 적용했을 때와 같은 결과를 주는 경우, 
# 즉 f(f(x)) ≡ f(x)인 경우 멱등법칙을 만족한다고 한다. 
# 예를 들어, 절댓값 함수는 멱등법칙을 만족한다: abs(abs(x)) ≡ abs(x).
# 어떤 이항연산은 두 같은 값에 적용되었을 때 항상 그 값을 결과로 주는 경우 멱등법칙을 만족한다고 한다. 
# 예를 들어, 두 값의 최댓값을 주는 연산은 멱등법칙을 만족한다: max(x, x) ≡ x. 
# 단항연산에 대한 정의는 이항연산에 대한 정의의 특수화이다.
# 어떤 이항 연산이 주어지고, 두 같은 값을 피연산자로 할 때 그 값이 결과로 나오는 경우 그 값을 이 연산에 대한 멱등원이라고 한다. 
# 예를 들어, 수 1은 곱셈의 멱등원이다: 1 × 1 = 1.
# 합집합·교집합 연산, 논리곱·논리합 연산, 그리고 일반적으로 격자의 이음과 만남 연산은 모두 이항연산으로서 멱등성을 갖는다.
# 항등사상과 상수사상은 필연히 멱등 함수
# 실수 또는 복소수 변수의 절댓값 함수, 실변수의 바닥 함수는 모두 멱등 함수
# 위상 공간 X의 부분집합 U를 U의 폐포로 대응시키는 함수는 X의 멱집합 P(X)에 정의된 함수로 멱등성을 가진다. 
# 이러한 함수는 폐포연산의 한 예이다, 모든 폐포연산은 멱등성을 만족한다.
# 통계학에서의 분산, 산술 평균 같은 함수는 멱등성을 만족한다.


# f(x)
# add_ten(num) 는 Idempotence 함수가 아니다
def add_ten(num):
    return num + 10

print(add_ten(10))
print(add_ten(add_ten(10)))

# Idempotence
# f(f(x)) = f(x)
#   f(f(10)) = 30 | f(10) = 20

# Idempotence 예제
print(abs(-10))
print(abs(abs(-10)))
print(abs(abs(abs(-10))))
# abs(-10) == 10
# abs(10) == 10
# abs(10) == 10

# Idempotence
a = 10
print('Address of a is {}'.format(id(a)))
a = a = 10
print('Address of a is {}'.format(id(a)))
a = a = a = 10
print('Address of a is {}'.format(id(a)))
a = 10
print('Address of a is {}'.format(id(a)))
