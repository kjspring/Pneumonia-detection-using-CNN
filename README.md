# Pneumonia-detection-using-CNN

## Background
In the United States, pneumonia is the second most likely reason a person is admitted to a hospital, behind the birth of a child. Over 1 million adults will be admitted for pneumonia and complications each year. There are many clinical presentations of pneumonia from mild disease with limited shortness of breath and productive cough to severe disease with fever, respiratory distress, and sepsis. Due to the wide spectrum of associated clinical features, pneumonia is a one of the differential diagnosis when assessing acute respiratory illnesses.

Pneumonia will keep an inflicted person's lungs from getting enough oxygen into their blood and is caused by inflamation around the air sacs of lungs. These air sacs may be filled with fluid or pus. Infections of fungi, viruses, or bacteria, or irritation from environmental factors may lead to pneumonia. According to the Center for Disease Control and Prevention (CDC) there are 14.4 deaths caused by pneumonia per 100,000 people in the population. That is about 50,000 death a year in the United States.

Early detection is critical in preventing death due to pneumonia. According to guidelines by the American Thoracic Society and Infectious Disease Society of America, the presence of an opacity on chest imaging in a patient with a compatible clinical syndrome is the gold standard for diagnosis of pneumonia. A radiologist will interpret the x-ray and look for white spots, called infiltrates. Once diagnosed, treatment can begin to remove the excess fluid in the lungs.

## Business Problem

The Association of American Medical Colleges (AAMC) projects to have a serious shortage of radiologists by 2033. This is in contrast of the increase in medical imaging of about 5% a year. A shortage of radiologists will lead to worse patient outcomes as the turnaround time for them to make a diagnosis on the medical image increases.

Our company, United Healthcare, is an medical insurance company that provides health insurance through private and Affordable Care Act (ACA) health insurance exchanges. We are expanding our coverage to more rural clients and hospitals but this is where the shortage of specialty care such as radiology is in crisis. Reducing the bottleneck in pneumonia diagnosis will reduce the time a patient is admitted to the hospital and reduce costs associated with this care.

With the increase cost and lower supply of radiologists, United Healthcare needs to develop an application to classify chest x-ray images of with pneumonia or not (normal). Those predicted to have pneumonia would be forwarded to a radiologist for a confirmed diagnosis. This will lessen the burden and cost of radiologists reviewing chest x-rays that are not indicative of pneumonia.

## Stakeholders
- United Healthcare executives
- Healthcare workers

Convolutional Neural Networks (CNN) is a machine learning technique that reduces the high dimensionality of images without losing its information. CNNs have outperformed other machine learning algorithms in image classification.

![1_vkQ0hXDaQv57sALXAJquxA.jpg](attachment:1_vkQ0hXDaQv57sALXAJquxA.jpg)

While densly connected neural networks learn global patterns in ther input feature space, convolution layers learn local paterns, that are found in 2-dimensional windows. This allows CNNs to learn patterns that are translation-invariant, something learned in one part of the image can be reused in another part. CNNs can also learn spatial heirarchies of patterns. The first layer of a CNN learns small local patterns such as edges. The next layer will learn larger patterns.

![CNN spatial hierarchies](img/spatial_hierarchy.PNG)
