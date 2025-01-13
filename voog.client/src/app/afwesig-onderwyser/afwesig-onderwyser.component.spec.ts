import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AfwesigOnderwyserComponent } from './afwesig-onderwyser.component';

describe('AfwesigOnderwyserComponent', () => {
  let component: AfwesigOnderwyserComponent;
  let fixture: ComponentFixture<AfwesigOnderwyserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AfwesigOnderwyserComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AfwesigOnderwyserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
