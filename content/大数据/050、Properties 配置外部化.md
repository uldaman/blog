Title: 050��Properties �����ⲿ��
Author: Martin
Date: 2016-08-01 17:27
Summary: JAVA �е� Properties �ļ���һ�������ļ�, ��Ҫ���ڱ��������Ϣ.

[TOC]

ת��: [Java �� Properties ���ʹ��](http://www.2cto.com/px/201006/47834.html)

Java �е� Properties �ļ���һ�������ļ�, ��Ҫ���ڱ��������Ϣ, �ļ�����Ϊ `*.properties`, ��ʽΪ�ı��ļ�, �ļ��������Ǹ�ʽ�� "**��=ֵ**" �ĸ�ʽ, �� Properties �ļ���, ������ "**#**" ����ע��, Properties �ļ��� Java ������õ��ĵط��ܶ�, �����ܷ���.

# Properties �ļ�
һ�� Properties �ļ�������: `test.properties`

```ini
#################################
#   ���̱���Ӧ�� IcisReport �������ļ� #
#   ����: 2006��11��21�� #
#################################
#
#   ˵��:ҵ��ϵͳ TopIcis �ͱ���ϵͳ IcisReport �Ƿ����
#   �ɷֿ����𵽲�ͬ�ķ�������, Ҳ���Բ���ͬһ������
#   ����; IcisReprot ��Ϊ������ web Ӧ�ó������ʹ���κ�
#   �� Servlet �������� J2EE ���������𲢵�������, Ҳ����
#   ͨ��ҵ��ϵͳ�Ľӿڵ�����Ϊҵ��ϵͳ��һ������Ӧ��.
#
#   IcisReport �� ip
IcisReport.server.ip=192.168.3.143
#   IcisReport �Ķ˿�
IcisReport.server.port=8080
#   IcisReport ��������·��
IcisReport.contextPath=/IcisReport
```
<br>
# Properties ��
Java �� `Properties` �������� Properties �ļ�, `Properties` ������ڰ� `Java.util` ��, ����̳��� `Hashtable`.

- `getProperty(String  key)`, ��ָ���ļ��ڴ������б�����������. Ҳ����ͨ������ key , �õ� key ����Ӧ�� value.
- `load(InputStream inStream)`, ���������ж�ȡ�����б� (����Ԫ�ض�) . ͨ����ָ�����ļ� (����˵����� `test.properties` �ļ�) ����װ������ȡ���ļ��е����� **��\-ֵ** ��. �Թ� `getProperty(String  key)` ������.
- `setProperty(String key, String value)`, ���� `Hashtable` �ķ��� `put`. ��ͨ�����û���� `put` ���������� **��\-ֵ** ��.
- `store(OutputStream out, String comments)`, ���ʺ�ʹ�� `load` �������ص� `Properties` ���еĸ�ʽ, ���� `Properties` ���е������б� (����Ԫ�ض�) д�������. �� `load` �����෴, �÷����� **��\-ֵ** ��д�뵽ָ�����ļ���ȥ.
- `propertyNames()`, �õ������ļ��� key �� `Enumeration`, ͨ�� `Enumeration` �� `hasMoreElements()` �� `nextElement()` �������ܱ������� Properties.
- `clear()`, �������װ�ص� **��\-ֵ** ��. �÷����ڻ������ṩ.

# ��ȡ Properties �ļ�
Java��ȡ Properties �ļ��ķ����кܶ�.

������õĻ���ͨ�� `java.lang.Class` ��� `getResourceAsStream(String name)` ������ʵ��, ���¿�����������:

`InputStream in = getClass().getResourceAsStream("��ԴName");`

��Ϊ����д�����, �ô�һ���㹻; ������������Ҳ����:

`InputStream in = new BufferedInputStream(new FileInputStream(filepath));`

# ʵ��
```java
 // ���� Properties �ೣ�õĲ���
 public class TestProperties {
     // ���� Key ��ȡ Value
     public static String GetValueByKey(String filePath, String key) {
         Properties pps = new Properties();
         try {
             InputStream in = new BufferedInputStream (new FileInputStream(filePath));
             pps.load(in);
             String value = pps.getProperty(key);
             System.out.println(key + " = " + value);
             return value;

         }catch (IOException e) {
             e.printStackTrace();
             return null;
         }
     }

     // ��ȡ Properties ��ȫ����Ϣ
     public static void GetAllProperties(String filePath) throws IOException {
         Properties pps = new Properties();
         InputStream in = new BufferedInputStream(new FileInputStream(filePath));
         pps.load(in);
         Enumeration en = pps.propertyNames(); // �õ������ļ�������

         while(en.hasMoreElements()) {
             String strKey = (String) en.nextElement();
             String strValue = pps.getProperty(strKey);
             System.out.println(strKey + "=" + strValue);
         }

     }

     // д�� Properties ��Ϣ
     public static void WriteProperties (String filePath, String pKey, String pValue) throws IOException {
         Properties pps = new Properties();

         InputStream in = new FileInputStream(filePath);
         // ���������ж�ȡ�����б�����Ԫ�ضԣ�
         pps.load(in);
         // ���� Hashtable �ķ��� put, ʹ�� getProperty �����ṩ������.
         // ǿ��Ҫ��Ϊ���Եļ���ֵʹ���ַ���. ����ֵ�� Hashtable ���� put �Ľ��.
         OutputStream out = new FileOutputStream(filePath);
         pps.setProperty(pKey, pValue);
         // ���ʺ�ʹ�� load �������ص� Properties ���еĸ�ʽ��
         // ���� Properties ���е������б�����Ԫ�ضԣ�д�������
         pps.store(out, "Update " + pKey + " name");
     }

     public static void main(String [] args) throws IOException{
         // String value = GetValueByKey("Test.properties", "name");
         // System.out.println(value);
         // GetAllProperties("Test.properties");
         WriteProperties("Test.properties","long", "212");
     }
 }
```
<br>
