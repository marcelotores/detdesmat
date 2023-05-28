from matplotlib import pyplot as plt
rep = [0.3333333333333333, 0.5454545454545454, 0.4, 0.6153846153846154, 0.8235294117647058, 1.0, 0.75, 0.75, 0.8, 0.8, 0.7142857142857143, 0.75, 0.5, 0.4, 0.8, 0.8235294117647058, 0.9047619047619048, 0.4, 0.7333333333333333, 0.8571428571428571, 0.8260869565217391, 0.7, 0.5, 0.7647058823529411, 0.8, 0.8636363636363636, 0.7619047619047619, 0.8, 0.7727272727272727, 0.8333333333333334, 0.8095238095238095, 0.9230769230769231, 0.9705882352941176, 0.9166666666666666, 0.8666666666666667, 0.7407407407407407, 0.8214285714285714, 0.8823529411764706, 0.8666666666666667, 0.88, 0.95, 0.7333333333333333, 0.6923076923076923, 0.8333333333333334, 0.8928571428571429, 0.9090909090909091, 0.9069767441860465, 0.8863636363636364, 0.8095238095238095, 0.7948717948717948, 0.8947368421052632, 0.975609756097561, 1.0, 0.875, 0.7894736842105263, 0.5, 0.5, 0.72, 0.851063829787234, 0.8301886792452831, 0.9019607843137255, 0.9259259259259259, 0.9056603773584906, 0.9574468085106383, 0.9215686274509803, 0.9333333333333333, 0.9090909090909091, 0.8, 0.8181818181818182, 0.25, 0.8918918918918919, 0.9130434782608695, 0.8653846153846154, 0.875, 0.8333333333333334, 0.8695652173913043, 0.9318181818181818, 0.851063829787234, 0.7948717948717948, 0.6923076923076923, 0.42857142857142855, 0.3333333333333333, 0.9166666666666666, 0.8974358974358975, 0.8333333333333334, 0.9215686274509803, 0.8888888888888888, 0.8833333333333333, 0.8627450980392157, 0.8541666666666666, 0.7575757575757576, 0.45454545454545453, 0.6, 0.375, 0.2, 0.25, 0.9166666666666666, 0.8620689655172413, 0.8648648648648649, 0.9130434782608695, 0.9069767441860465, 0.8727272727272727, 0.8260869565217391, 0.7727272727272727, 0.7575757575757576, 0.6363636363636364, 0.9444444444444444, 0.8666666666666667, 0.9285714285714286, 0.8, 0.75, 0.8, 0.8421052631578947, 0.9024390243902439, 0.9183673469387755, 0.9272727272727272, 0.851063829787234, 0.8837209302325582, 0.7894736842105263, 0.7272727272727273, 0.8421052631578947, 0.7777777777777778, 0.8636363636363636, 0.6923076923076923, 0.25, 0.7666666666666667, 0.8888888888888888, 0.8363636363636363, 0.7735849056603774, 0.8163265306122449, 0.82, 0.9259259259259259, 0.8771929824561403, 0.8378378378378378, 0.7857142857142857, 0.6, 1.0, 0.9047619047619048, 0.8409090909090909, 0.8333333333333334, 0.7868852459016393, 0.864406779661017, 0.8, 0.7792207792207793, 0.8441558441558441, 0.8867924528301887, 0.8181818181818182, 0.5384615384615384, 1.0, 0.9166666666666666, 0.8372093023255814, 0.8545454545454545, 0.8169014084507042, 0.8611111111111112, 0.8933333333333333, 0.8767123287671232, 0.8823529411764706, 0.9019607843137255, 0.7333333333333333, 0.6363636363636364, 0.9565217391304348, 0.918918918918919, 0.8596491228070176, 0.8765432098765432, 0.8571428571428571, 0.8505747126436781, 0.8311688311688312, 0.9, 0.8780487804878049, 0.5833333333333334, 0.875, 0.92, 0.9130434782608695, 0.890625, 0.945054945054945, 0.8604651162790697, 0.8705882352941177, 0.863013698630137, 0.9411764705882353, 0.8888888888888888, 0.7083333333333334, 0.875, 0.8, 0.9444444444444444, 0.8607594936708861, 0.9166666666666666, 0.8446601941747572, 0.8089887640449438, 0.8133333333333334, 0.7884615384615384, 0.7142857142857143, 0.6111111111111112, 0.6, 0.6666666666666666, 0.9019607843137255, 0.8227848101265823, 0.9134615384615384, 0.8857142857142857, 0.8452380952380952, 0.8611111111111112, 0.7962962962962963, 0.8620689655172413, 0.8636363636363636, 0.8, 0.3333333333333333, 1.0, 0.8823529411764706, 0.96, 0.9541284403669725, 0.9113924050632911, 0.875, 0.7441860465116279, 0.8275862068965517, 0.9230769230769231, 0.9333333333333333, 0.9666666666666667, 0.8431372549019608, 0.922077922077922, 0.9310344827586207, 0.8888888888888888, 0.9183673469387755, 0.6857142857142857, 0.7878787878787878, 0.90625, 0.9166666666666666, 0.9333333333333333, 0.8076923076923077, 0.9148936170212766, 0.9245283018867925, 0.918918918918919, 0.9259259259259259, 0.38461538461538464, 0.8, 0.88, 0.8846153846153846, 0.25, 0.7647058823529411, 0.8421052631578947, 0.9411764705882353, 1.0, 1.0, 0.75, 0.9565217391304348, 0.9629629629629629]
good = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 8, 14, 0, 0, 2, 3, 3, 4, 4, 5, 6, 5, 2, 8, 14, 19, 0, 4, 11, 18, 19, 14, 8, 13, 16, 19, 16, 16, 17, 20, 0, 17, 24, 33, 33, 26, 20, 23, 30, 26, 22, 19, 11, 9, 10, 25, 30, 39, 39, 34, 31, 34, 40, 29, 21, 15, 5, 4, 18, 40, 44, 46, 50, 48, 45, 47, 42, 20, 16, 9, 1, 0, 33, 42, 45, 42, 35, 40, 41, 40, 31, 9, 3, 1, 0, 0, 33, 35, 40, 47, 40, 53, 44, 41, 25, 5, 3, 3, 2, 3, 22, 25, 32, 42, 39, 48, 38, 34, 25, 14, 17, 13, 13, 8, 9, 8, 16, 37, 45, 51, 40, 38, 30, 32, 32, 21, 19, 9, 0, 0, 1, 23, 40, 46, 41, 40, 41, 50, 50, 31, 22, 9, 0, 0, 1, 19, 37, 45, 48, 51, 52, 60, 65, 47, 27, 7, 0, 0, 1, 22, 36, 47, 58, 62, 67, 64, 60, 46, 22, 7, 0, 0, 0, 22, 34, 49, 71, 66, 74, 64, 54, 36, 14, 7, 0, 0, 0, 23, 42, 57, 86, 74, 74, 63, 48, 32, 17, 7, 0, 0, 0, 20, 51, 68, 99, 87, 72, 61, 41, 20, 11, 3, 0, 0, 0, 12, 46, 65, 95, 93, 71, 62, 43, 25, 19, 8, 0, 0, 0, 3, 42, 60, 96, 104, 72, 56, 32, 24, 24, 14, 0, 0, 0, 0, 29, 43, 71, 81, 56, 45, 24, 26, 29, 22, 0, 0, 0, 0, 14, 21, 43, 49, 34, 25, 5, 16, 22, 23, 0, 0, 0, 0, 0, 1, 13, 16, 16, 14, 1, 12, 22, 26]
distance = [77.88420486450195, 49.28547922770182, 88.0009817481041, 25.643053770065308, 13.162865774972099, 2.2247449159622192, 27.635785420735676, 27.635785420735676, 44.26375961303711, 58.04469737410545, 14.569921684265136, 24.031139214833576, 16.345906257629395, 69.18726348876953, 61.42070184648037, 18.753799387386866, 9.648133328086452, 16.807735443115234, 53.02444715933366, 80.94015680419074, 66.43184646179802, 62.2894577894892, 41.818247362971306, 5.357151728409987, 5.349401205778122, 18.249546320814837, 14.409067451953888, 24.4414189979434, 10.428936243057251, 2.4306530714035035, 53.25140197136823, 14.395665888984999, 15.494442387060685, 4.960100076415322, 64.20181213433926, 62.32645980715752, 33.861130901004955, 15.323544637362163, 13.934922837294065, 4.356187717481093, 20.266970082333213, 8.311542077498002, 6.491164472368029, 21.481079435348512, 44.828887414932254, 17.28611349662145, 24.63128269635714, 21.27378235719143, 55.79614478349686, 54.10899140373353, 33.080928693799414, 16.63094389438629, 8.00897242282999, 2.32156735374814, 16.519785594940185, 7.7657242774963375, 10.207155346870422, 48.57941450013055, 52.36429170966149, 31.71595983071761, 32.46254135992216, 55.857051630020145, 38.2472410351038, 23.95441172387865, 22.56371340599466, 29.74121023927416, 20.521146047115327, 23.50640668720007, 44.46372307671441, 37.269290924072266, 51.797773187810726, 14.823488672574362, 12.324015829298231, 16.105953883557092, 43.56022100448608, 21.19850167632103, 29.756309160372105, 27.36525768339634, 43.99713046704569, 40.52145216200087, 48.370466232299805, 41.26742172241211, 56.417190262765594, 20.631672927311488, 25.5089011490345, 30.085550216918296, 49.86621000468731, 27.04966946817794, 26.724039096723903, 29.220794328829136, 46.28567439079285, 13.134924411773682, 14.080285867055258, 14.080285867055258, 18.079047441482544, 37.38453483581543, 72.07984230735086, 19.030078315734862, 24.05679665878415, 14.38054942233222, 27.170345437832367, 32.05031528323889, 37.520045142424735, 28.009921841761646, 45.13341207504273, 27.17970609664917, 48.882026966880346, 43.260853694035454, 42.880008697509766, 33.982449531555176, 137.1564304563734, 25.739322304725647, 55.60313059389591, 34.45277156700959, 37.366537729899086, 21.658328030623643, 34.47380041182041, 55.08889605497059, 36.44287843704224, 53.04082765802741, 39.9942608512938, 25.82000445751917, 21.4734108573512, 53.382545471191406, 248.98995971679688, 24.91496797748234, 18.550960743427275, 12.751788782036822, 34.78721088316382, 54.632103404402734, 50.45587365510987, 46.221092290878296, 36.40211122751236, 21.020023776638894, 27.35107352516868, 53.792591677771675, 248.98995971679688, 31.271340351355704, 26.715469724423176, 37.86191180017259, 47.468777333696686, 50.34675064040165, 47.37574174083196, 34.88093825976054, 33.048312359589794, 37.10521413924846, 36.92664935853746, 65.80563592910767, 248.98995971679688, 42.019150869412854, 32.610656294557785, 25.216841854947678, 37.064840921040236, 57.00617690624729, 64.19719486450082, 52.56417322717607, 29.752033158143362, 50.03494365837263, 38.195791461251, 31.748373985290527, 41.747779255563565, 29.52166915991727, 26.561544603231003, 21.958156229744496, 35.181357403596245, 42.11433027886056, 32.78593594953418, 26.50040066242218, 40.33206012182765, 2.0552185603550504, 31.748373985290527, 60.66943595202073, 22.72272703193483, 19.407373844531545, 22.519586942916693, 32.592517785123874, 25.00090987617905, 33.31705223000239, 45.592726876338325, 54.335556857287884, 56.94489087777979, 34.797873394829885, 54.71639568209648, 29.613147616386414, 29.973672063911664, 32.75892044679083, 43.10026456021715, 30.79931597246064, 28.8360628808131, 32.08179128751522, 6.0470489919185635, 6.34884081103585, 6.411179701487224, 88.97741614778836, 43.264825655066446, 19.831444021371695, 29.305585807248164, 41.24846901944888, 36.73943295948942, 33.321539440462665, 18.768953789112178, 1.0878767013549804, 1.1604656357514231, 20.95859633386135, 137.27970377604166, 67.676521332491, 23.549763466914495, 15.47440992295742, 18.735467187487163, 19.539721371399033, 27.080115118197032, 27.57595184072852, 0.4809291909138362, 5.165662889679273, 19.55891352891922, 103.71300850654471, 27.538204861241717, 22.33006462412821, 19.339152777636492, 31.22867285779544, 41.82570105658637, 42.790933564305305, 13.238561300130991, 9.19209337234497, 10.211960987611251, 140.50252301352364, 69.5725797471546, 45.151393721270004, 43.122300442384216, 29.94507670402527, 52.907409386634825, 9.256115913391113, 7.699569851160049, 0.2650432586669922, 6.379017342691836, 229.11569213867188, 66.89008866823636, 67.59894949197769, 67.60856539011002, 58.57161283493042, 37.336307525634766, 29.973395546277363, 17.875201767141167, 9.496000161537758]

plt.hist(rep, rwidth=0.9)
plt.xlabel('Rep')
plt.ylabel('Qtd. Imagens')
plt.title('Poisson')
plt.show()

plt.title('Poisson')
plt.hist(good, rwidth=0.9)
plt.xlabel('Qtd. correspondencias')
plt.ylabel('Qtd. Imagens')
plt.show()