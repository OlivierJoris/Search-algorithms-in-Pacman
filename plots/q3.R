own <- c(log(568), log(8945))
zero <- c(log(568), log(12983))

colors <- c("blue", "green", "blue", "green")

barplot(cbind(own, zero), beside = TRUE, names.arg = c("Own g(n) & h(n)", "Own g(n) & h(n)=0"), col = colors, ylim = c(0,10), main = "A* with different heuristics", ylab = "Logarithmic values")
legend("bottom", legend = c("Score", "Expanded nodes"), col=c("blue", "green"), pch = c(15,15))
