import { Component, Input, OnDestroy } from '@angular/core';
import { ApiService } from '../api.service';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-voog',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './voog.component.html',
  styleUrl: './voog.component.css'
})
export class VoogComponent implements OnDestroy {

  lookupForm = new FormGroup({
    teacherCode: new FormControl(''),
    day: new FormControl(''),
  });
  voogLearners = null

  TeacherCodeSubsctiption: Subscription
  TeacherCode = ''

  onSubmit() {
    let Day = Number(this.lookupForm.value['day'])

    this.api.getTeacherlessLearnersVoog(this.TeacherCode, Day).subscribe(data => {
      this.voogLearners = data
      console.log(data)
    })
  }

  ngOnDestroy() {
    this.TeacherCodeSubsctiption.unsubscribe()  
  }

  constructor (private api: ApiService) {
    this.TeacherCodeSubsctiption = api.TeacherCodeSource$.subscribe(
      TeacherCode => {
        this.TeacherCode = TeacherCode
      }
    )
  }
}
