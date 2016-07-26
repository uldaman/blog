Title: 048��ʹ�� addBatch() ���Ч��
Author: Martin
Date: 2016-07-25 17:50
Summary: ʹ��������������� JDBC Ч��

[TOC]

**References**:<br>
[JDBC �� PreparedStatement ��������ʹ�������� executeBatch()](http://www.cnblogs.com/tommy-huang/p/4540407.html)<br>
[ʹ�� JDBC �� addBatch() �������Ч��](http://www.cnblogs.com/husam/p/3830225.html?utm_source=tuicool&utm_medium=referral)

���������� SQL ������ʱ����ʹ�� addBatch, ����Ч���Ǹ�Щ, ������Խ��Խ�����ֳ���.

**Statement** �ӿ�������������:

```java
// �������� SQL ������ӵ��� Statement ����ĵ�ǰ�����б���. ͨ�����÷��� executeBatch ��������ִ�д��б��е�����.
void addBatch(String sql)
// ��һ�������ύ�����ݿ���ִ��, ���ȫ������ִ�гɹ�, �򷵻ظ��¼�����ɵ�����.
int[] executeBatch()
```
<br>
����: ��������ÿ�������һ��Ԫ�صĸ��¼�������ɵ����� (�����е�ÿ��Ԫ��Ϊ: �ɹ������������, ִ��������Ӱ�����ݿ��������ĸ��¼���), �����Ԫ�ظ��ݽ�������ӵ����е�˳������.

**PreparedStatement** �ӿ���:<br>
��д�� `addBatch()` �ķ���, `executeBatch()` ��û����д.

```java
// ��һ�������ӵ��� PreparedStatement �����������������.
void addBatch()
```
<br>
��Ϊ���ݿ�Ĵ����ٶ��Ƿǳ����˵�, �����������ܴ�, ִ��Ч�ʼ���, `addBatch()` ������ sql ���װ�ص�һ��, Ȼ��һ���͵����ݿ�ִ��, ִ��ֻ��Ҫ�̵ܶ�ʱ��.

����˵˵ `PreparedStatement` ����Ҫ�� `addbatch()` ��ʹ��.

```java
// 1.��������(��绰����)
Connection connection = getConnection();

// 2.���Զ� Commit (���Ӳ���һ��һ����, ȫ��������������, Ȼ��һ������)
connection.setAutoCommit(false);

// 3.Ԥ����SQL���, ֻ����һ��Ŷ, Ч�ʸ߰�.(����һ�������ӵķ���, �Ժ�Ҫ������ô�����Ӻ�, ��������.)
PreparedStatement statement = connection.prepareStatement("INSERT INTO TABLEX VALUES(?, ?)");

// 4.��һ����һ��, Ȼ���������
// ��¼1
statement.setInt(1, 1);
statement.setString(2, "Cujo");
statement.addBatch(); // ������ִ�����ӵ� PreparedStatement �����������������

// ��¼2
statement.setInt(1, 2);
statement.setString(2, "Fred");
statement.addBatch(); // ������ִ�����ӵ� PreparedStatement �����������������

// ��¼3
statement.setInt(1, 3);
statement.setString(2, "Mark");
statement.addBatch(); // ������ִ�����ӵ� PreparedStatement �����������������

// ����ִ������3�����. һ������, ��ˬ
int[] counts = statement.executeBatch(); // ��������ӵ������������е���������һ�ι��ύ�����ݿ���ִ��

// Commit it ����ȥ, ������(DB)����
connection.commit();
```
