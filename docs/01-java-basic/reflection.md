---
title: "反射原理与应用"
freq: 2
status: done
summary: "通过 Class 对象在运行时拿到类的字段、方法、构造器并调用；Spring 的 IoC、动态代理、注解处理都靠它。代价是性能开销和破坏封装。"
---

# 反射原理与应用

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/java/basis/reflection.html)

## 一句话答案

反射是在**运行时**获取类的信息（字段、方法、构造器、注解）并调用它们的能力，入口是 `Class` 对象。Spring 的依赖注入、动态代理、MyBatis 的结果映射、JUnit、Jackson 序列化都靠反射。缺点是比直接调用慢、绕过了访问控制、编译器检查不到错误。

## 展开（1–2 分钟能讲完）

**常用 API**：

```java
Class<?> c = Class.forName("com.x.User");
Object u = c.getDeclaredConstructor().newInstance();
Field f = c.getDeclaredField("name");
f.setAccessible(true);              // 访问 private
f.set(u, "Tom");
Method m = c.getMethod("hello", String.class);
m.invoke(u, "hi");
```

`getMethods()` 拿 public 方法（含继承的），`getDeclaredMethods()` 拿本类所有方法（含 private，不含继承的）。

**原理**：类加载后，方法区里有类的元数据，堆里有一个对应的 `Class` 对象作为访问入口。反射就是通过 Class 对象查元数据，再调用方法。

**`Method.invoke` 的实现**：早期版本前 15 次用 native 实现调用，超过阈值后**动态生成字节码**（`MethodAccessor`），之后就和普通调用差不多快（叫 inflation）。JDK 18 起改用 `MethodHandle` 实现（JEP 416）。

## 图解

```mermaid
flowchart LR
  A["@Autowired private UserService us"] --> S["Spring 扫描字段<br/>field.getAnnotation(Autowired.class)"]
  S --> B["从容器拿到 UserService 实例"]
  B --> F["field.setAccessible(true)<br/>field.set(bean, instance)"]
```

## 追问链

- **获取 Class 的三种方式？** `User.class`（编译期已知，不触发初始化）；`obj.getClass()`；`Class.forName("全限定名")`（默认会触发类的初始化，执行静态代码块）。还有 `classLoader.loadClass()`，只加载不初始化。
- **反射为什么慢、怎么优化？** 慢在：方法参数要装箱成 `Object[]`、要做访问检查、查找方法要遍历和比较字符串、JIT 难以内联。优化：把 `Method`/`Field` 对象**缓存**起来，不要每次都 `getMethod`；`setAccessible(true)` 关掉访问检查；用 `MethodHandle`（JIT 能更好地优化）；性能敏感的地方用代码生成（如 MapStruct 编译期生成映射代码，比 BeanUtils 反射拷贝快很多）。
- **注解的原理？** 注解本质是继承了 `Annotation` 的接口。`@Retention(RUNTIME)` 的注解会保留在 class 文件里，运行时 `getAnnotation()` 返回一个 JDK 动态代理生成的对象，读属性时从一个 Map 里取值。`SOURCE` 级的注解（如 `@Override`、Lombok）只在编译期给编译器或注解处理器用。
- **反射能修改 final 字段吗？** 普通实例的 final 字段可以通过 `setAccessible(true)` 修改，但如果是编译期常量会被内联，改了也看不到效果；static final 字段在新版本 JDK 里不能改。record 和隐藏类的 final 字段不能改。
- **JDK 9 模块化之后的限制？** 模块没有 `opens` 的包，`setAccessible(true)` 会抛异常（JDK 16 起默认强封装），老框架要加 `--add-opens`。

## 我的项目里

TODO：项目里有没有自己写过用反射的代码（比如自定义注解 + AOP、通用的对象转换工具）？
